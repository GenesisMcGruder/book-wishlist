import React from "react";
import Bookcard from "./Bookcard";

function Wishlist({wishlists, addToWishlist, deleteFromWishlist, user}){
    if (!wishlists || wishlists.length === 0) {
        return (
            <div className="wishlist">
                <h1 className="wishlist-header">Wishlist</h1>
                <p>No items in wishlist.</p>
            </div>
        );
    }
    const wishlistsCards = wishlists.map((book)=>(
        <Bookcard 
        key={book.title}
        book={book} 
        addToWishlist={addToWishlist} 
        deleteFromWishlist={deleteFromWishlist}
        wishlists={wishlists}
        user={user}
        />
    ));
    return (
        <div className="wishlist">
            <h1 className="wishlist-header">Wishlist</h1>
            {wishlistsCards}
        </div>
    )
}

export default Wishlist;