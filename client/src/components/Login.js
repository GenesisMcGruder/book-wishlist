import { useFormik } from "formik";
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import * as Yup from 'yup';

function Login({setUser, fetchBooks, setIsLoggedIn, fetchWishlist}){
    const navigate = useNavigate()
    const formik = useFormik({
        initialValues:{
            username: "",
            password: ""
        },
        onSubmit: (values) => {
            fetch('login', {
                method: 'POST',
                headers: {
                    "Content-Type":"application/json",
                },
                body:JSON.stringify(values, null , 2),
            }).then(
                (res) => {
                    if(res.status === 200){
                        setUser(values)
                        setIsLoggedIn(true)
                        fetchBooks()
                        fetchWishlist()
                        navigate('/Books')
                    } 
                }
            )
        },
        validatationSchema: Yup.object({
            username: Yup.string().required('Username is required'),
            password: Yup.string().required('Password is required'),
        }) 

    })
    return(
        <div className="form-case">
            <form className="form" onSubmit={formik.handleSubmit}>
            <h1>Login</h1>
            <label>Username:</label>
            <input className="form-input"
            name="username"
            type="text"
            value={formik.values.username}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}/>
            <div className="error">
                {formik.errors.username && formik.touched.username && formik.errors.username}
            </div><br/>
            <label>Password:</label>
            <input className="form-input"
            name="password"
            type="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}/>
            <div className="error">
            {formik.errors.password && formik.touched.password && formik.errors.password}</div><br/>
            <button className="login-btn" type="submit">Submit</button>
        </form>
        <Link to='/Signup' className="login-to-signup">Don't have an account? Signup here.</Link>
        </div>
    )
}

export default Login;