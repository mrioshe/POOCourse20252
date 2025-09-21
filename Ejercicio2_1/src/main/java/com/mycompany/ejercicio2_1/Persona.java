/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio2_1;

/**
 *
 * @author Mauricio
 */
public class Persona {
    String nombre;
    String apellidos;
    String numeroDocumentoIdentidad;
    int anhoNacimiento;
    
    Persona(String nombre, String apellidos, String numeroDocumentoIdentidad, int anhoNacimiento){
    this.nombre=nombre;
    this.apellidos=apellidos;
    this.numeroDocumentoIdentidad = numeroDocumentoIdentidad;
    this.anhoNacimiento = anhoNacimiento;
    }
    
    void imprimir(){
    System.out.println("Nombre = " + nombre);
    System.out.println("Apellido = " + apellidos);
    System.out.println("Numero de comento de identidad = " + numeroDocumentoIdentidad);
    System.out.println("Año de nacimiento = " + anhoNacimiento);
    System.out.println();
 
    }
}
