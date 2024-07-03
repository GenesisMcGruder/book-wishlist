import React from "react";
import { Link, useNavigate } from "react-router-dom";

function Logout({user, handleLogout}){
    const navigate = useNavigate()
    function handleDelete(){
        fetch(`/logout/${user.id}`,{
            method:'DELETE',
        })
        .then(()=>{
            handleLogout()
            navigate('/')
        })
    }
    return(
        <div>
            <h1 className="logout-header">Are you sure you want to Logout?</h1>
            <p className="yes-no"onClick={handleDelete}>Yes| <Link to='/Books'>No</Link></p>
        </div>
    )
}

export default Logout;