/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicioresuelto4;

/**
 *
 * @author Mauricio
 */
public class EjercicioResuelto4 {

    public static void main(String[] args) {
        double EDJUAN = 9;
        double EDALBER, EDANA, EDMAMA;
        EDALBER = Calculos.calcular_edalber(EDJUAN);
        EDANA = Calculos.calcular_edana(EDJUAN);
        EDMAMA = Calculos.calcular_edmama(EDJUAN,EDALBER,EDANA);
        System.out.println("la edades son: ");
        System.out.println("Juan " + EDJUAN);
        System.out.println("Ana " + EDANA);
        System.out.println("Alberto " + EDALBER);
        System.out.println("Mama " + EDMAMA);
    }
}

