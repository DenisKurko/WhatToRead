import React, { Component } from "react";
import { 
    BrowserRouter as Router, 
    Routes, 
    Route, 
    Link, 
    Navigate
} from "react-router-dom";

import Search from "./search";
import Profile from "./profile";
import AddBook from "./addbook"

export default class Home extends Component{
    constructor(props){
        super(props);
    }

    render() {
        return(
        <Router>
            <Routes>
                <Route path='/' element={<p>HOME PAGE</p>}/>
                <Route path='/profile' element={<Profile/>}/>
                <Route path='/search' element={<Search/>}/>
                <Route path='/addbook' element={<AddBook/>}/>
            </Routes>
        </Router>
        );
    }
}