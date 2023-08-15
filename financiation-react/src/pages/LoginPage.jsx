import React, {useContext} from "react";
import '../assets/styles/LoginPage.css'
import Logo from "../assets/images/PRUEBA.PNG";
import {Button, Container, FloatingLabel, Form} from "react-bootstrap";
import {Link} from "react-router-dom";
import AuthContext from "../context/AuthContext";

const LoginPage = () => {
    let {loginUser} = useContext(AuthContext)
    return (
        <Container fluid className="general">
            <Container fluid className="image-container">
                <img src={Logo} alt="Logo del ministerio de finanzas"/>
            </Container>
            <Form onSubmit={loginUser}>
                <Container>
                    <FloatingLabel className='floatingLabel' label="Usuario">
                        <Form.Control placeholder="Usuario" type="text" name="username" required/>
                    </FloatingLabel>
                </Container>
                <Container>
                    <FloatingLabel className='floatingLabel' label="Contraseña">
                        <Form.Control placeholder="Contraseña" type="password" name="password" minLength='6' required/>
                    </FloatingLabel>
                </Container>
                <Container fluid>
                    <Button type="submit">Acceder</Button>
                </Container>
            </Form>
            <Link to="/signin/"><Button variant="link" className="link">No tengo una cuenta</Button></Link>
            <Link to="/reset-password/"><Button variant="link" className="link">Me olvidé la contraseña</Button></Link>
        </Container>
    )
};

export default LoginPage;