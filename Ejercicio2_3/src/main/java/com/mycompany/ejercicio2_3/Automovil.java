/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio2_3;

/**
 *
 * @author Mauricio
 */
public class Automovil {
    String marca;
    int modelo;
    int motor;
    int numeroPuertas;
    int cantidadAsientos;
    int velocidadMaxima;
    tipoColor color;
    tipoCom tipoCombustible;
    tipoA tipoAutomovil;
    int velocidadActual;
    
    Automovil(String marca,int modelo, int motor, tipoCom tipoCombustible, tipoA tipoAutomovil,
            int numeroPuertas, int cantidadAsientos, int velocidadMaxima, tipoColor color){
    
    this.marca=marca;
    this.modelo=modelo;
    this.motor=motor;
    this.tipoCombustible=tipoCombustible;
    this.tipoAutomovil=tipoAutomovil;
    this.numeroPuertas=numeroPuertas;
    this.cantidadAsientos=cantidadAsientos;
    this.velocidadMaxima=velocidadMaxima;
    this.color=color;
    }
    
    String getMarca(){
        return marca;
    }
    
    int getModelo(){
        return modelo;
    }
    
    int getMotor() {
        return motor;
    }
    
    tipoCom getTipoCombustible() {
        return tipoCombustible;
    }
    
    tipoA getTipoAutomovil(){
        return tipoAutomovil;
    }
    
    int getNumeroPuertas() {
        return numeroPuertas;
    }
    
    int getCantidadAsientos() {
        return cantidadAsientos;
    }
    
    int getVelocidadMaxima() {
        return velocidadMaxima;
    }
    
    tipoColor getColor(){
        return color;
    }
    
    int VelocidadActual() {
        return velocidadActual;
    }
    
    void setMarca (String marca){
        this.marca=marca;
    }
    
    void setModelo(int modelo) {
        this.modelo = modelo;
    }
    
    void setMotor(int motor) {
        this.motor = motor;
    }
    
    void setTipoCombustible(tipoCom tipoCombustible) {
        this.tipoCombustible = tipoCombustible;
    }
    
    void setTipoAutomovil(tipoA tipoAutomovil) {
        this.tipoAutomovil = tipoAutomovil;
    }
    
    void setNumeroPuertas(int numeroPuertas) {
        this.numeroPuertas = numeroPuertas;
    }
    
    void setCantidadAsientos(int cantidadAsientos) {
        this.cantidadAsientos = cantidadAsientos;
    }
    
    void setVelocidadMaxima(int velocidadMaxima) {
        this.velocidadMaxima = velocidadMaxima;
    }
    
    void setColor(tipoColor color) {
        this.color = color;
    }
    
    void setVelocidadActual(int velocidadActual) {
        this.velocidadActual = velocidadActual;
    }
    
    void acelerar(int incrementoVelocidad) {
        
        if ((velocidadActual+incrementoVelocidad)<velocidadMaxima){
            velocidadActual=velocidadActual + incrementoVelocidad;
        }else{
            System.out.println("No se puede incrementar a una velocidad superior a la máxima del automovil.");
        }
    }
    
    void desacelerar(int decrementoVelocidad) {
        
        if ((velocidadActual-decrementoVelocidad)>0){
            velocidadActual=velocidadActual - decrementoVelocidad;
        }else{
            System.out.println("No se puede decrementar a una velocidad negativa.");
        }
    }
    
    void frenar(){
        velocidadActual=0;
    }
    
    double calcularTiempoLlegada(int distancia){
        return distancia/velocidadActual;
    }
    
    void imprimir(){
        System.out.println("Marca= " + marca);
        System.out.println("Modelo= " + modelo);
        System.out.println("Motor= " + motor);
        System.out.println("Tipo de combustible= " + tipoCombustible);
        System.out.println("Tipo de automóvil= " + tipoAutomovil);
        System.out.println("Número de puertas= " + numeroPuertas);
        System.out.println("Cantidad asientos= " + cantidadAsientos);
        System.out.println("Velocidad máxima= " + velocidadMaxima);
        System.out.println("Color= " + color);
    }
    
}
