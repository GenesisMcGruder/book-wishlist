import React, { useEffect, useState } from "react";
import Bookcard from "./bookcard";

function Books(){
    const [books, setBooks] = useState([])
    useEffect(()=>{
        fetch('/books')
        .then((res)=> res.json())
        .then((data)=> setBooks(data))
    }, [])

    const bookCard = books.map((book)=> <Bookcard key={book.id} book={book}/>)
return (
    <>
    <div className="books">
        {bookCard}
    </div>
    </>
)
}

export default Books;