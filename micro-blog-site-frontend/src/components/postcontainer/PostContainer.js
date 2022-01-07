import React,{useEffect} from "react";
import Post from "../post/Post";
import './styles.css'
import { getAllPosts } from "../../utility/PostsUtility";
const PostContainer = (posts) => {
    useEffect(() => {
        console.log(getAllPosts())
    }, [])
    return(
        <div className="posts_container">
            <Post/>
            <Post/>
            <Post/>
        </div>
    )
}
export default PostContainer;