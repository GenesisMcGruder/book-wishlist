import React from "react";
import { Link } from "react-router-dom";


function App() {
    return (
        <>
        <h1>Welcome!</h1>
        <p><Link to='/Signup'>Signup</Link> | <Link to='/Login'>Login</Link></p>
        </>
    )
}

export default App;