#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// =================================================================
// (just some io helper for c, see readline_def.h)
char *read_section_start();
void read_section_end();
bool is_eof();

char *skip_until(const char *set);
char *skip_n(int n);

int *read_next_int(int *out) {
    char *str;
    if ((str = skip_until("-0-9")) == NULL) {
        printf("error: unexpected eof\n");
        return NULL;
    }
    char *endptr = NULL;
    long long int r = strtoll(str, &endptr, 10);
    if (str == endptr) {
        printf("error: invalid int format\n");
        return NULL;
    }
    *out = (int) r;
    skip_n(endptr - str);
    return out;
}

// =================================================================
// main

void Q1() {
    int M, N, P, Q;
    read_next_int(&M);
    read_next_int(&N);
    read_next_int(&P);
    read_next_int(&Q);
    read_section_end();
    if (P == 0) {  // avoid divided by 0 as c has portable no way to catch it
        printf("error: P is 0\n");
        return;
    }
    int candy = N * M;
    int ans = 0;
    int paper = 0;
    while (candy > 0) {
        ans += candy;
        paper += candy;
        int old_candy = candy;
        candy = paper / P * Q;
        if (candy > old_candy) {
            printf("error: inf loop\n");
            return;
        }
        paper %= P;
    }
    printf("%d\n", ans);
}


int main() {
    while (!is_eof()) {  // exit when EOF
        read_section_start();
        Q1();
    }
    return 0;
}

#include "readline_def.h"
