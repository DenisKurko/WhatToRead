import React, { Component } from "react";
import { createRoot } from "react-dom/client";

export default class App extends Component{
    constructor(props){
        super(props);
    }
    render() {
        return <h1>TEST REACT TEST</h1>;
    }
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);