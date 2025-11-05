/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejerciciop406;

/**
 *
 * @author Mauricio
 */


public class Vendedor {
    private String nombre;
    private String apellidos;
    private Integer edad; // null = no asignada

    public Vendedor(String nombre, String apellidos) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = null;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getApellidos() {
        return apellidos;
    }


    public Integer getEdad() {
        return edad;
    }

    public void verificarEdad(int edad) {
        if (edad < 18) {
            throw new IllegalArgumentException("El vendedor debe ser mayor de 18 años.");
        }
        if (edad >= 0 && edad <= 120) {
            this.edad = edad;
        } else {
            throw new IllegalArgumentException("La edad no puede ser negativa ni mayor a 120.");
        }
    }

    public boolean tieneEdadAsignada() {
        return this.edad != null;
    }
}
