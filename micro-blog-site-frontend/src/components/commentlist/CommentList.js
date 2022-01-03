import React from 'react'
import Comment from '../comment/Comment';
import './styles.css'

const CommentList = () => {

    return(
        <div className='comment_list_container'>
            <Comment/>
            <Comment/>
            <Comment/>
            <Comment/>
            <Comment/>
        </div>
    )
}
export default CommentList;