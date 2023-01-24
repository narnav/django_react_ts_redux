import React from "react";
import "./App.css";
import { Outlet, Link } from "react-router-dom";
import { selectCartItems } from "./features/cart/cartSlice";
import { useAppSelector, useAppDispatch } from "./app/hooks";
import { selectLogged, logoutAsync } from "./features/Login/loginSlice";
function App() {
  const dispatch = useAppDispatch();
  const logged = useAppSelector(selectLogged || false);
  const cartItems = useAppSelector(selectCartItems || []);
  return (
    <div className="App">
      <nav style={{ borderBottom: "solid 1px", paddingBottom: "1rem" }}>
        <Link to="/Products">Products</Link> | <Link to="/about">About</Link> |{" "}
        <Link to="/categories">Categories</Link>|
        {logged ? (
          <button onClick={() => dispatch(logoutAsync())}>Logout</button>
        ) : (
          <Link to="/login">login</Link>
        )}
        |{" "}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          className="bi bi-basket3-fill"
          viewBox="0 0 16 16"
        >
          <path d="M5.757 1.071a.5.5 0 0 1 .172.686L3.383 6h9.234L10.07 1.757a.5.5 0 1 1 .858-.514L13.783 6H15.5a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5H.5a.5.5 0 0 1-.5-.5v-1A.5.5 0 0 1 .5 6h1.717L5.07 1.243a.5.5 0 0 1 .686-.172zM2.468 15.426.943 9h14.114l-1.525 6.426a.75.75 0 0 1-.729.574H3.197a.75.75 0 0 1-.73-.574z" />
        </svg>
        ({cartItems.length})
      </nav>
      <Outlet></Outlet>
    </div>
  );
}

export default App;
