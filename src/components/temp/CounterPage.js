import React from "react";
import { useState } from "react";

const CounterPage = () => {
    const [ counter, setCount ] = useState(0);

    const handleClick = () => {
        setCount(counter + 1)
        console.log("Clicked " + counter);

    }

    return (
        <div>
            <b style={{ borderBottom: '1px solid black', width: '18px', display: 'inline-block', textAlign: 'center' }}>{counter}</b>
            <button onClick={handleClick}>+1</button>
        </div>
    
    );
}

export default CounterPage;