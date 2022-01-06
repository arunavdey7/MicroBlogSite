import React from "react";
import Post from "../post/Post";
import './styles.css'

const PostContainer = () => {

    return(
        <div className="posts_container">
            <Post/>
            <Post/>
            <Post/>
        </div>
    )
}
export default PostContainer;