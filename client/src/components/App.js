import React, { useEffect, useState } from "react";
import Home from "./Home";
import Books from "./Books";
import NavBar from "./NavBar";
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";
import Signup from "./Signup";
import Login from "./Login";
import Wishlist from "./Wishlist";
import AppContext from "./AppContext";
import { useLocation } from "react-router-dom";
import Bookcard from "./Bookcard";
import UserProfile from "./UserProfile";
import Logout from "./Logout";


function App() {

  const [user,setUser] = useState([])
  const [books, setBooks] = useState([])
  const [wishlists, setWishlists] = useState([])
  const [showForm,setShowForm] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false)


  useEffect(()=>{
    fetch('check_session')
    .then((res)=> res.json())
    .then((data)=> {
      setUser(data)
      console.log(data)
      if (data && data.id){
        fetchBooks();
        fetchWishlist(data.id)
      } else{
        setBooks([]);
        setWishlists([])
      }
    })
      .catch((error)=> {
        console.error("Error checking session", error);
      })
  },[isLoggedIn])

  function fetchBooks() {
    fetch(`/books`)
      .then((res) => res.json())
      .then((data) => {
        setBooks(data);
      })
      .catch((error) => {
        console.error("Error fetching books:", error);
        setBooks([]);
      });
  }
  
  function fetchWishlist(userId) {
    fetch(`/wishlist_by_id/${userId}`)
      .then((res) => res.json())
      .then((data) => {
        setWishlists(data);
      })
      .catch((error) => {
        console.error("Error fetching wishlist:", error);
        setWishlists([]);
      });
  }

function addToWishlist(user,book){
  fetch('add_to_wishlist',{
      method: 'POST',
      headers:{
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          user_id: user.id,
          book_id: book.id
      }),
  })
  .then((res)=> res.json())
  .then((data)=>{
      console.log(data)
      console.log(user)
      setWishlists((wishlists)=> [...wishlists,data])
      fetchBooks()
      fetchWishlist(user.id)
  })
  .catch((error)=>{
    console.error("Error adding to wishlist:", error)
  })
}


function handleClick(){
    setShowForm((showForm) => !showForm)
}

function deleteFromWishlist(userId, bookId){
  fetch(`delete_from_wishlist/${userId}/${bookId}`, {
    method: 'DELETE',
  })
  .then((res)=> res.json())
  .then( () => {
    console.log("book successfully removed form wishlist")
    setWishlists((wishlists) => wishlists.filter((item)=> item.book_id !==bookId))
    fetchBooks()
    fetchWishlist(user.id)
  })
  .catch((error)=> {
    console.error("Error deleteing from wishlist:",error)
  })
}

function handleLogout(){
  setUser([null])
  setBooks([])
  setWishlists([])

}

const bookCards = books.map((book)=>(
  <Bookcard 
  key={book.id}
  book={book} 
  user={user} 
  addToWishlist={addToWishlist} 
  wishlists={wishlists} 
  deleteFromWishlist={deleteFromWishlist}
  />
));


    return (
      <Router> 
      <AppContext.Provider 
      value={{user, 
      bookCards, 
      wishlists, 
      handleClick, 
      showForm, 
      setUser,
      fetchBooks,
      fetchWishlist, 
      setIsLoggedIn,
      addToWishlist,
      deleteFromWishlist,
      handleLogout}}>
        <NavBarWrapper/>
        <Routes>
          <Route path="/" element={<Home />}/> 
          <Route path="/Signup" element={<Signup setUser={setUser} fetchBooks={fetchBooks} fetchWishlist={fetchWishlist}setIsLoggedIn={setIsLoggedIn}/>}/>
          <Route path="/Login" element={<Login setUser={setUser} fetchBooks={fetchBooks} fetchWishlist={fetchWishlist} setIsLoggedIn={setIsLoggedIn}/>}/>
          <Route path="/Books"element={
            <Books 
            bookCards={bookCards}  
            handleClick={handleClick} 
            showForm={showForm}
            fetchBooks={fetchBooks}/>} />
          <Route path="/Wishlist" element={
            <Wishlist 
            wishlists={wishlists} 
            addToWishlist={addToWishlist} 
            user={user} 
            deleteFromWishlist={deleteFromWishlist}/>}/>
          <Route path="/UserProfile" element={
            <UserProfile 
            user={user} 
            handleClick={handleClick} 
            showForm={showForm}
            setUser={setUser}
            setIsLoggedIn={setIsLoggedIn}/>}/>
          <Route path="/Logout" element={
            <Logout 
            user={user} 
            handleLogout={handleLogout} 
            setIsLoggedIn={setIsLoggedIn}/>}/> 
        </Routes>
        </AppContext.Provider>
    </Router>
    )
}
function NavBarWrapper(){
  const location = useLocation()
  return location.pathname !== "/"&& location.pathname !== '/Signup' && location.pathname !== '/Login' && <NavBar/>;
}

export default App;