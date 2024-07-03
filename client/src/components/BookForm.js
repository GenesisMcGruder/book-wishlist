import React from "react";
import {useFormik} from 'formik';
import * as Yup from "yup";


function BookForm({handleClick}){
        const formik = useFormik({
            initialValues:{
                title:"",
                author: "",
                image: "",
                summary: "",
                page_count: ""   
            },
            onSubmit: (values, actions) => {
                fetch('books',{
                    method:"POST",
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body:JSON.stringify(values),
                }).then(
                    (res)=>{
                        if (res.status === 200){
                            actions.resetForm()
                            handleClick()
                            console.log(values)
                        }
                    }
                )
            },
            validationSchema: Yup.object({
                title: Yup.string().required('Title required'),
                author: Yup.string().required('Author required'),
                image: Yup.string().required('Image required'),
                summary:Yup.string().required('Summary required'),
                page_count:Yup.number().integer().required('Page count required')
            })
        })
        return(
            <div className="form-case">
                <form className="form" onSubmit={formik.handleSubmit}>
                    {/* <h1 className="form-header">Books</h1> */}
                    <label>Title:</label>
                    <input className="form-input"
                    name="title"
                    type="text"
                    value={formik.values.title}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}/>
                    <div className="error">
                        {formik.errors.title && formik.touched.title && formik.errors.title}
                    </div><br/>
                    <label>Author:</label>
                    <input className="form-input"
                    name="author"
                    type="text"
                    value={formik.values.author}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}/>
                    <div className="error">
                        {formik.errors.author && formik.touched.author && formik.errors.author}
                    </div><br/>
                    <label>Image:</label>
                    <input className="form-input"
                    name="image"
                    type="text"
                    value={formik.values.image}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}/>
                    <div className="error">
                        {formik.errors.image && formik.touched.image && formik.errors.image}</div><br/>
                    <label>Summary:</label>
                    <input className="form-input"
                    name="summary"
                    type="text"
                    value={formik.values.summary}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}/>
                    <div className="error">
                        {formik.errors.summary && formik.touched.summary && formik.errors.summary}</div><br/>
                    <label>Page Count:</label>
                    <input className="form-input" 
                    name="page_count"
                    type="number"
                    value={formik.values.page_count}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}/>
                    <div className="error">
                        {formik.errors.pageCount && formik.touched.pageCount && formik.errors.pageCount}</div><br/>
                    <button className="form-input-submit" type="submit">Submit</button>
                </form>
            </div>
            
        )
    }
    
    
    export default BookForm;