import React from "react";
import './styles.css'

const Post = () => {

    return(
        <div className="post_body_container">
            <div className="post_thumbnail">
                <img height='147' width='235' src='https://picsum.photos/600'/>
            </div>
            <div className="post_content_container">
                <div className="post_title">
                   This is a post title.
                </div>
                <div className="post_description">
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                </div>
            </div>
        </div>
    )
}
export default Post;