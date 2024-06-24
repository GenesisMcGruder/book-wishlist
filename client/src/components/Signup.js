import React from "react";
import {useFormik} from 'formik';
import * as Yup from "yup";

function Signup(){
    const formik = useFormik({
        initialValues:{
            email:"",
            username: "",
            password: "",
            bio: ""   
        },
        onSubmit: (values) => {
            console.log('onSubmit', values);
        },
        validationSchema: Yup.object({
            email: Yup.string().required('Email is required').email('Invalid email'),
            username: Yup.string().required('Username is required'),
            password: Yup.string().required('Password is required'),
            bio:Yup.string().required('Bio is required')
        })
    })
    return(
        <>
        <h1>Signup</h1>
        <form className="form" onSubmit={formik.handleSubmit}>
            <label>Email:</label>
            <input className="form-input"
            name="email"
            type="text"
            value={formik.values.email}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}/>
            <div className="error">
                {formik.errors.email && formik.touched.email && formik.errors.email}
            </div><br/>
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
            <label>Bio:</label>
            <input className="form-input"
            name="bio"
            type="text"
            value={formik.values.bio}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}/>
            <div className="error">
            {formik.errors.bio && formik.touched.bio && formik.errors.bio}</div><br/>
            <button type="submit">Submit</button>
        </form>
        </>
    )
}


export default Signup;