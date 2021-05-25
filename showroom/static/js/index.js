$(function () {
    $('.countrylist').select2({
        ajax: {
            url: '/ajax/countrylist/',
            dataType: 'json'
        }
    });
    $('.filters').click((e) => {e.stopPropagation();$('.filters').addClass('active');}); //show filters
    $(document.body).click(() => {$('.filters').removeClass('active')}); //hide filters
    
    let searchFilters = {
        name: $('#name')[0].value,
        year: $('#year')[0].value,
        grapes: $('#grape')[0].value,
        country: getCountries('.countrylist'),
    };

    $('#name').change((e) => {searchFilters.name = $('#name')[0].value; getCatalog();});
    $('#grape').change((e) => {searchFilters.grapes = $('#grape')[0].value; getCatalog();});
    $('#year').change(function (e) {
        let value = parseInt($('#year')[0].value);
        if(!isNaN(value)) {
            let actualYear = new Date().getFullYear();
            value = value <= actualYear ? value : actualYear
            $('#year')[0].value = value;
            searchFilters.year = value;
        } else {
            $('#year')[0].value = '';
            searchFilters.year = '';
        }
        getCatalog();
    });
    $('.countrylist').on({
        "change.select2": function (e) {
            searchFilters.country = getCountries(this);
            getCatalog();
        }
    });
    
    getCatalog = function() {
        $.ajax({
            url: "/ajax/catalog/",
            dataType: 'json',
            data: searchFilters,
            success: function (response) {
                $('#catalog').empty();
                response.forEach(data => $('#catalog').append( wineCard(data) ) );
            },
            error: function () {
                console.log("error");
            }
        });
    };
    getCatalog();
});


getCountries = function(select) {
    let option = '';
    $(select).find(':selected').each((index) => {
        option += $(select).find(':selected')[index].innerHTML + ';';
    });
    return option.slice(0, -1);
};

//CRASH TEST ZONE
//learning about template string in JS




function wineCard(data) {
    return `
    <div class="card">
        <div class="imgContainer">
            <img src="/media/${data.image}" alt="${data.name} picture">
        </div>
        <div class="name">
            <h3>${data.name}</h3>
        </div>
        <div class="wineinfo">
            <p>${data.country}<br>${data.region}</p>
            <p>${data.grapes} ${data.year}</p>
        </div>
        <div class="desc">
            <p>
                ${data.description}
            </p>
        </div>
    </div>
    `;
};