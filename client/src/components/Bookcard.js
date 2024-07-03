import React, {useEffect, useState} from "react";

function Bookcard({book, addToWishlist, wishlists, deleteFromWishlist, user}){
    const {id,title, author, image, summary, page_count} = book
    const [isAdded, setIsAdded] = useState(false)

    useEffect(()=>{
        const existInWishlist = wishlists && wishlists.length > 0 && wishlists.some(wishlistBook => wishlistBook.id === id);
        setIsAdded(existInWishlist)  
    },[wishlists,id])

    function handleClick(){
        if (isAdded){
            deleteFromWishlist(user.id, book.id)
            setIsAdded(false)
            console.log(`${title} has successfully removed from wishlist`)
        } else{
            addToWishlist(user,book)
            setIsAdded(true)
            console.log(`${title} has successfully added to wishlist`)
        }
    }

    return(
        <div className="book-card">
            <img className="book-img" src={image} alt='book img'/>
            <h3>{title}</h3>
            <h4>Author: {author}</h4>
            <p>Summary: {summary}</p>
            <p>Page Count: {page_count}</p>
            <button className="wishlist" onClick={handleClick}>{isAdded?"Remove from Wishlist":"Add to Wishlist"}</button>
        </div>
    )
}

export default Bookcard;