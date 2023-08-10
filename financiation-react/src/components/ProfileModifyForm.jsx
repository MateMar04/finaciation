import { Button, Col, Container, FloatingLabel, Form, Row } from "react-bootstrap";
import React from "react";
import "../assets/styles/ProfileModifyForm.css"

export const ProfileModifyForm = () => {
    return (
        <Container fluid>
        <h2>Cuenta</h2>

        <Form>
            <Row >

                <Col lg={4} className="profile-form-col1 ">
                    <p className="ab">Modificar nombre de usuario</p>
                </Col>
            </Row>
            <Row>

                <Col lg={4} className="profile-form-col2 ">
                    <FloatingLabel className='floatingLabel' label="Usuario">

                        <Form.Control className="profile-fc" placeholder="Usuario" type="text" name="username"
                            required />
                    </FloatingLabel>

                </Col>
                <Col lg={3} className="profile-form-col button-container"></Col>
                <Col lg={5} className="profile-form-col button-container">

                    <Button className="change-password">
                        Aplicar
                    </Button>
                </Col>


            </Row>
                <Row className="profile-form-row">
                    <Col lg={6} className="profile-form-col">
                        <FloatingLabel className='floatingLabel' label="Nombre">
                            <Form.Control className="profile-fc" placeholder="Nombre" type="text" name="username"
                                required />
                        </FloatingLabel>
                    </Col>
                    <Col lg={6} className="profile-form-col">
                        <FloatingLabel className='floatingLabel' label="Apellido">
                            <Form.Control className="profile-fc" placeholder="Apellido" type="text" name="username"
                                required />
                        </FloatingLabel>
                    </Col>
                </Row>
                <Row className="profile-form-row">
                    <Col lg={6} className="profile-form-col">
                        <FloatingLabel className='floatingLabel' label="CUIL">
                            <Form.Control className="profile-fc" placeholder="CUIL" type="text" name="username"
                                required />
                        </FloatingLabel>
                    </Col>
                    <Col lg={6} className="profile-form-col">
                        <FloatingLabel className='floatingLabel' label="Número de Teléfono">
                            <Form.Control className="profile-fc" placeholder="Número de Teléfono" type="text"
                                name="username" required />
                        </FloatingLabel>
                    </Col>
                </Row>
                <Container>
                    <Button className="sumbit-button" type="submit">Guardar</Button>
                </Container>
            </Form>
        </Container>
    )
}

export default ProfileModifyForm