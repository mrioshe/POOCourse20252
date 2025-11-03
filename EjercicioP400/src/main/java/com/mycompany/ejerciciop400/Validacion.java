/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejerciciop400;

/**
 *
 * @author Mauricio
 */
public class Validacion {
    
    public static double calcularDivision(double numerador, double denominador){
        double cociente=0;
        try{
            if (denominador >0){
            return cociente = numerador/denominador;
            }
        }
        
        catch (ArithmeticException e) { 
            System.out.println("División por cero"); 
            return cociente;
        } 
        return cociente;
    }
    
    public static String obtenerTexto (String mensaje){
        try{
        if (mensaje.isEmpty()==false){
            return mensaje;
                }
            }
        catch(Exception ex){
            return "Error: " + ex.getMessage();
            }
        return "Text vacìo";
        }
    
            
    
}
