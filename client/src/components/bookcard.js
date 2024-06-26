import React from "react";

function Bookcard({book}){
    const {title, author, image, summary, pageCount} = book
    return(
        <div className="book-card">
            <img className="book-img" src={image} alt='book img'/>
            <h3>{title}</h3>
            <h4>Author: {author}</h4>
            <h4>Summary: {summary}</h4>
            <h4>Page Count: {pageCount}</h4>
            <button className="wishlist">Wishlist</button>
        </div>
    )
}

export default Bookcard;