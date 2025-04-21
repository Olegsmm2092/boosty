import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { increment, decrement } from "../../store/slicers/counterSlice";

const NewCounterPage = () => {
    const counter = useSelector((state) => state.counter.value);
    const dispatch = useDispatch();

    return (
        <div>
            <b style={{ borderBottom: '1px solid black', width: '18px', display: 'inline-block', textAlign: 'center' }}>{counter}</b>
            <button onClick={() => dispatch(increment(6))}>+6</button>
            <button onClick={() => dispatch(decrement())}>-1</button>
        </div>
    
    );
}

export default NewCounterPage;