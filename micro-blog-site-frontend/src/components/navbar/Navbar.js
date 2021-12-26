import React,{useState, useEffect} from 'react' 
import './styles.css'

const Navbar = () => {

    const [dropdownState, setDropdownState] = useState(false)
    const [userLoggedInStatus, setUserLoggedInStatus] = useState(true)
    const [count, setCount] = useState(2)

    // For controlling collapsed Navbar dropdown
    const showDropDown = () => {
        if(count % 2 == 0)
        {
            setDropdownState(true)
            setCount(count + 1)
        }
        else
        {
            setDropdownState(false)
            setCount(count + 1)
        }      
    }
    
    return(
        <>
       <div className = "navbar">
           <div className="logo_container">
              <div>
                <h1 className="brand_text">SuperBlog</h1>
              </div>
           </div>
           <div className="link_container">
                <div className="link_box">
                    <div>
                        <a href="#"><h3>Home</h3></a>
                    </div>
                </div>
                <div className="link_box">
                    <div>
                        <a href="#"><h3>Latest</h3></a>
                    </div>
                </div>
                <div className="link_box">
                    <div>
                        <a href="#"><h3>Categories</h3></a>
                    </div>
                </div>
                {userLoggedInStatus === true ? 
                    <div className="link_box user_name_container">
                        <h2>Arunav</h2>
                    </div> :
                    <div className="link_box user_name_container" style={{fontSize:10},{width:100}}>
                        <h2>Log In</h2>
                    </div>
                }
                {userLoggedInStatus &&       
                    <div className="link_box user_name_container profile_pic">
                        <img src="https://picsum.photos/100" height="40" width="40" className="profile_pic"></img>
                    </div>
                }
                {userLoggedInStatus &&
                    <div className="link_box user_name_container">
                        <i class="fa fa-sign-out fa-2x"></i>
                    </div>
                }   
                
           </div>
           <div onClick={showDropDown} className="hamburger">
               <div>
                    <i class="fa fa-bars fa-2x"></i>
               </div>
           </div>
       </div>
       <div className="dropdown_menu_container">
            <div className="dropdown_menu" style={dropdownState === true ? {display:"flex"} : {display:"none"}}>
                <div className="dropdown_menu_item">
                    <a href="#"><h3>Home</h3></a>
                </div>
                <div className="dropdown_menu_item">
                    <a href="#"><h3>Latest</h3></a>
                </div>
                <div className="dropdown_menu_item">
                    <a href="#"><h3>Categories</h3></a>
                </div>
                {userLoggedInStatus &&
                    <div className="dropdown_menu_item">
                        <a href="#"><h3>Arunav Dey</h3></a>
                    </div>
                }
                {
                    userLoggedInStatus &&
                    <div className="dropdown_menu_item">
                        <a href="#"><h3>Sign Out</h3></a>
                    </div>
                }
            </div>
       </div>
       </>
    )
}
export default Navbar;