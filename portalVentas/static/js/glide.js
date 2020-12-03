$tarjetaSlider = document.querySelectorAll('.slider__elemento');

window.addEventListener('load', function () {
    new Glider(document.querySelector('.slider__lista'), {
      slidesToShow: 1,
      slidesToScroll: 2,
      draggable: true,
      //dots: '.slider__indicadores',
      responsive: [
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            rewind:true,
            arrows: {
              prev: '.slider__anterior',
              next: '.slider__siguiente'
            },
          }
        },
        {
          breakpoint: 900,
          settings: {
            slidesToShow: $tarjetaSlider.length%2 === 0 ? 2 : 3,
            slidesToScroll: 1,
            rewind:true,
            arrows: {
              prev: '.slider__anterior',
              next: '.slider__siguiente'
            },
          }
        },
        {
          breakpoint: 1400,
          settings: {
            slidesToShow: $tarjetaSlider.length%2 === 0 ? 4 : 3,
            slidesToScroll: 2,
            rewind:true,
            arrows: {
              prev: '.slider__anterior',
              next: '.slider__siguiente'
            },
          }
        }
      ]
    });
  });