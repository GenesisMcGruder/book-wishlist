import React from "react";
import BookForm from "./BookForm";

function Books({bookCards, showForm, handleClick}){

return (
    <>
    <div className="books">
        <h1 className="books-header">Books</h1>
        {showForm ? <BookForm handleClick={handleClick}/>: null}
        <div className="show-book-form" onClick={handleClick}>Add a Book</div>
        <div className="book-card-display">
            {bookCards}   
        </div>
    </div>
    </>
)
}

export default Books;