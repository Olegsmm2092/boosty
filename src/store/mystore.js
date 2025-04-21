import { configureStore } from "@reduxjs/toolkit";
import counterReducer from './slicers/counterSlice';

export const mystore = configureStore(
    {
        reducer: {
            counter: counterReducer
        }
    }
)