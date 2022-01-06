import React,{useState} from "react";
import './styles.css'

const Post = () => {

    const [liked,setLikedStatus] =  useState(false);
    const [likesCount, setLikesCount] = useState(0);
    const [commentsCount, setCommentsCount] = useState(6);

    const like = () => {
        if(liked)
        {
            setLikedStatus(false)
            setLikesCount(likesCount - 1)
        }
        else
        {
            setLikedStatus(true)
            setLikesCount(likesCount + 1)
        }
        
    }
    return(
        <div className="post_body_container">
            <div className="post_thumbnail">
                <img className='responsive' src='https://picsum.photos/420/200'/>
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
                <div className='utility_bar_container'>
                    <div className='utility_icon_labels'>
                        <i className='fa fa-share'></i>
                        <span className='label_span'>Share</span>
                    </div>
                    <div>
                        <i className='fa fa-comment'></i>
                        <span className='label_span'>{commentsCount} </span>
                    </div>
                    {
                        liked ? 
                        <div onClick={like}>
                            <i className='fa fa-heart'></i>
                            <span className='label_span'>{likesCount}</span>
                        </div>
                        :
                        <div onClick={like}>
                            <i className='fa fa-heart-o'></i>
                            <span className='label_span'>{likesCount}</span>
                        </div>
                    }
                    
                </div>
            </div>
        </div>
    )
}
export default Post;