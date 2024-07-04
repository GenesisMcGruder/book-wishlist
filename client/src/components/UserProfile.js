import React from "react";
import UpdateUser from "./UpdateUser";

function UserProfile({user, handleClick, showForm, setUser, setIsLoggedIn}){
    const {username, email, bio} = user
    return (
        <div className="user-profile">
            <h3>Username: {username}</h3>
            <h3>Email: {email}</h3>
            <h3>Bio: {bio}</h3>
            {showForm ? <UpdateUser user={user} setUser={setUser} setIsLoggedIn={setIsLoggedIn}/>: null}
            <div className="show-update-form" onClick={handleClick}>Update Profile</div>
        </div>
    )
}

export default UserProfile;