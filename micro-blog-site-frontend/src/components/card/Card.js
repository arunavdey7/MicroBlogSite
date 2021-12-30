import React from 'react';
import './styles.css'

const Card = () => {

    return(
        <div className='card_body_container'>
            <div className='image_container'>
                <div className='thumbnail'>
                    <img className='image_tag' src="https://picsum.photos/500/500"></img>
                </div>
            </div>
            <div className='content_container'>
                <div className='card_post_title'>
                    <h1 className='card_title_text' style={{marginTop:0},{marginBottom:0}}>Post Title</h1>
                </div>
                <div className='card_post_content'>
                    <p>
                        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
                    </p>
                </div>
            </div>
        </div>
    )
}
export default Card;