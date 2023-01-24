import { configureStore, ThunkAction, Action } from "@reduxjs/toolkit";
import cartSlice from "../features/cart/cartSlice";
import catsReducer from "../features/cats/catsSlice";
import loginReducer from "../features/Login/loginSlice";
import prodsReducer from "../features/products/prodsSlice";

export const store = configureStore({
  reducer: {
    login: loginReducer,
    cats: catsReducer,
    prods: prodsReducer,
    cart: cartSlice,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
