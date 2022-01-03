import React from 'react';
import './styles.css'

const Comment = () => {
return (
    <div className='comment_container'>
        <div className='commentor_name_container'>
            <div className='commentor_name'>
                <div>
                    <h3 className='commentor_name_text'>Arunav Dey</h3>
                </div>
                <div>
                    <i className='fa fa-trash delete_comment_icon'></i>
                </div>
            </div>
        </div>
        <div className='gap'>
        </div>
        <div className='comment_content_container'>
            <div className='comment_content'>
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum is simply dummy text of the printing and typesetting industry
            </div>
        </div>
        <div className='gap'>
        </div>
        <div className='time_stamp'>
            <h4 className='time_stamp_text'>7:17 P.M, 2nd Jan 2022</h4>
        </div>
        
        
    </div>
)
}
export default Comment;