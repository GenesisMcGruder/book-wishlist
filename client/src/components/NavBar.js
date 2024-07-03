import React from "react";
import { NavLink} from "react-router-dom";
import "./styling.css";

function NavBar(){

    return(
        <nav className="background">
        <NavLink to="/Books"
        className="nav-link">
            Books
        </NavLink>
        <NavLink to="/Wishlist"
        className="nav-link">
            Wishlist
        </NavLink>
        <NavLink to="/UserProfile"
        className="nav-link">
            Profile
        </NavLink>
        <NavLink to="/Logout"
        className="nav-link">
            Logout
        </NavLink>
    </nav>
    )
}

export default NavBar;