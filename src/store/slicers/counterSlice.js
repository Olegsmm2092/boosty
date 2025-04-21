import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value: 0,
}

const counterSlice = createSlice(
    {
        name: "counter",
        initialState: initialState,
        reducers: {
            increment: (state, action) => {
                state.value += action.payload;
            },
            decrement: (state) => {
                state.value -= 1;
            }
        }
    }
)

export const { increment, decrement } = counterSlice.actions;
export default counterSlice.reducer;