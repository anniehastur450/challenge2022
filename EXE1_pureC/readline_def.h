#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// =================================================================
// (just some io helper for c)
#pragma region Collapse
#pragma region [new_varbuf(), varbuf_element_at(), varbuf_clear(), varbuf_add(), delete_varbuf()]
#define _VARBUF_INIT_CAP 16
typedef struct {
    int size;   // element size
    char *ptr;  // contains at most cap*size bytes
    int cap;    // capacity
    int num;    // number of elements
} VARBUF;
void *varbuf_element_at(VARBUF *varbuf, int index) {
    return varbuf->ptr + index * varbuf->size;
}
void varbuf_clear(VARBUF *varbuf) {
    memset(varbuf->ptr, 0, varbuf->size * varbuf->cap);
    varbuf->num = 0;
}
void varbuf_add(VARBUF *varbuf, void *element, int count) {
    // new num = num + count
    while (varbuf->cap < varbuf->num + count) {
        varbuf->cap *= 2;
    }
    varbuf->ptr = (char *)realloc(varbuf->ptr, varbuf->size * varbuf->cap);
    void *dst = varbuf_element_at(varbuf, varbuf->num);
    memcpy(dst, element, count * varbuf->size);
    varbuf->num += count;
}
void varbuf_create(VARBUF *varbuf, int element_size) {
    varbuf->size = element_size;
    varbuf->ptr = (char *)malloc(element_size * _VARBUF_INIT_CAP);
    varbuf->cap = _VARBUF_INIT_CAP;
    varbuf_clear(varbuf);
}
void varbuf_free(VARBUF *varbuf) {
    free(varbuf->ptr);
    memset(varbuf, 0, sizeof(VARBUF));
}
VARBUF *new_varbuf(int element_size) {
    VARBUF *res = (VARBUF *)malloc(sizeof(VARBUF));
    varbuf_create(res, element_size);
    return res;
}
void delete_varbuf(VARBUF *varbuf) {
    varbuf_free(varbuf);
    free(varbuf);
}
#pragma endregion

#pragma region [_read_line()]
#define _BUFFER_SIZE 2048
struct {
    VARBUF *varbuf;
    int len;  // because varbuf->num includes the \0 !!!
    int line_len;
    int offset;
    bool is_eof;
} _read_buf = { 0 };
char *_read_line_0() {
    if (_read_buf.varbuf == NULL) {  // varbuf init
        _read_buf.varbuf = new_varbuf(sizeof(char));
    }
    varbuf_clear(_read_buf.varbuf);
    char buf[_BUFFER_SIZE];
    char *p;
    while ((p = fgets(buf, _BUFFER_SIZE, stdin))) {
        int len = strlen(buf);
        varbuf_add(_read_buf.varbuf, buf, len);
        if (buf[len - 1] == '\n') {  // ignore \r for now
            char term = 0;
            varbuf_add(_read_buf.varbuf, &term, 1);  // add \0
            break;
        }
    }
    _read_buf.len = strlen(_read_buf.varbuf->ptr);
    _read_buf.line_len = strcspn(_read_buf.varbuf->ptr, "\r\n");
    _read_buf.offset = 0;
    if (_read_buf.varbuf->num == 0) {  // encounter EOF
        _read_buf.is_eof = true;
        return NULL;
    }
    return _read_buf.varbuf->ptr;
}
char *_read_line() {
    if (_read_buf.line_len == 0) {  // begining of section
        char *r;
        while ((r = _read_line_0()) != NULL && _read_buf.line_len == 0) ;
        return r;
    } else {
        // middle of section
        char *r = _read_line_0();
        if (!r) return NULL;
        if (_read_buf.line_len == 0) return NULL;
        return r;
    }
}
#pragma endregion

#pragma endregion

char *get_read_ptr() {
    return _read_buf.varbuf->ptr + _read_buf.offset;
}

char *read_line() {  // return NULL if section end
    if (_read_buf.line_len == 0) return NULL;  // section already end
    return _read_line();
}

char *peek() {
    if (_read_buf.offset >= _read_buf.len) {  // rem len <= 0
        return read_line();
    }
    return (char *)varbuf_element_at(_read_buf.varbuf, _read_buf.offset);
}

char *read() {
    char *r = peek();
    if (r) {
        _read_buf.offset++;
    }
    return r;
}

char *skip_n(int n) {
    while (n > 0) {
        if (!read()) return NULL;
        n--;
    }
    return peek();
}

bool is_in_set(const char *set, int c) {
    const char *p = set;
    int prev = *p;
    while (*p) {
        p++;
        if (*p == '-') {
            p++;
            if (prev <= c && c <= *p) {
                return true;
            }
        } else if (c == prev) {
            return true;
        }
        prev = *p;
    }
    return false;
}

char *skip_until(const char *set) {  // set: character set
    int set_len = strlen(set);
    char *r;
    while ((r = peek()) != NULL) {
        // check if *r in set
        if (is_in_set(set, *r)) return r;
        read();  // move next
    }
    return r;
}

// ----------------------------------------------------------------

char *read_section_start() {
    return _read_line();
}

void read_section_end() {
    while (read_line()) ;
}

bool is_eof() {
    return _read_buf.is_eof;
}
