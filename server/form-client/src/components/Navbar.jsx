import { Link } from "react-router-dom";
import styled from "styled-components";

export function Navbar() {
  return (
    <Nav>
      <Link to="/form">Formulario A</Link>
      <Link to="/form-b">Formulario B</Link>
      <Link to="/form-c">Formulario C</Link>
      <Link to="/form-d">Formulario D</Link>
      <Link to="/form-e">Formulario E</Link>
      <Link to="/form-f">Formulario F</Link>
    </Nav>
  );
}

const Nav = styled.nav`
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 1rem;
  a {
    color: #fff;
    text-decoration: none;
  }
`;
