import React from "react";
import "./index.css";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Books from "./components/Books";
import Home from "./components/Home";
import Signup from "./components/Signup";
import Login from "./components/Login";
import UserProfile from "./components/UserProfile";

const router = createBrowserRouter([{
  path:'/',
  element: <Home/>,
  errorElement: <div>404 Not Found</div>
},{
  path:'/Books',
  element: <Books/>,
  errorElement: <div>404 Not Found</div>
},{
  path:'/Signup',
  element: <Signup/>,
  errorElement: <div>404 Not Found</div>
},{
  path:'/Login',
  element: <Login/>,
  errorElement: <div>404 Not Found</div>
},{
  path:'/UserProfile',
  element:<UserProfile/>,
  errorElement: <div>404 Not Found</div>
}]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode> 
);

// const container = document.getElementById("root");
// const root = createRoot(container);
// root.render(<App />);
