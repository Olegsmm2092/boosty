import React from "react";
import CounterPage from "../temp/CounterPage";
import NewCounterPage from "../temp/NewCounterPage";

const HomePage = () => {
    return (
        <div className="homePageClass">
            <h1> This is HomePage </h1>
            <CounterPage/>
            <CounterPage/>
    
            <NewCounterPage/>
            <NewCounterPage/>
        </div>
    );
}

export default HomePage;