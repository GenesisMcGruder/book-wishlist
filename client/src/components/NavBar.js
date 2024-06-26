import React from "react";
import { NavLink } from "react-router-dom";

function NavBar(){
    return(
        <nav className="background">
        <NavLink to="/"
        className="nav-link">
            Home
        </NavLink>
        <NavLink to="/Books"
        className="nav-link">
            Books
        </NavLink>
    </nav>
    )
}

export default NavBar;