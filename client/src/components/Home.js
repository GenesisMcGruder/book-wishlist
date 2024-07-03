import React from "react";
import { Link } from "react-router-dom";

function Home() {
    return (
        <>
        <h1 className="welcome">Welcome to Wishlist!</h1>
        <p className="welcome-btn"><Link to='/Signup'>Signup</Link> | <Link to='/Login'>Login</Link></p>
        </>
    )
}

export default Home;