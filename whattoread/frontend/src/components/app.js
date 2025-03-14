import React, { Component } from "react";
import { createRoot } from "react-dom/client";
import Home from "./home";

export default class App extends Component{
    constructor(props){
        super(props);
    }

    render() {
        return (
        <div>
            <Home />
        </div>
        );
    }
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);