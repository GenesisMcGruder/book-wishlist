import { useFormik } from "formik";
import React from "react";
import * as Yup from 'yup';

function Login(){
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
                        console.log(values)
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
        <>
        <h1>Login</h1>
        <form className="form" onSubmit={formik.handleSubmit}>
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
            type="text"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}/>
            <div className="error">
            {formik.errors.password && formik.touched.password && formik.errors.password}</div><br/>
            <button className="submit" type="submit">Submit</button>
        </form>
        </>
    )
}

export default Login;