import React from 'react'
import Slider from "react-slick";

import Card from '../card/Card'
import './styles.css'

const CardCarousel = () =>
{
    var settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 4,
        slidesToScroll: 4,
        initialSlide: 0,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 0,
              slidesToScroll: 0,
              infinite: true,
              dots: true
            }
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              initialSlide: 2
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              initialSlide: 0,
              
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              initialSlide: 0,
              dots: false
          
            }
          }
        ]
      };
    return(
        <div className='slider_container'>
            <Slider {...settings}>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
                <div className='card'>
                    <Card/>
                </div>
            </Slider>
      </div>
    )
}
export default CardCarousel;