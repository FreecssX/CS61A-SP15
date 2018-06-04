(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)
  	)
  )

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond ((> x 0) 1)
  	   ((= x 0) 0)
  	   ((< x 0) -1))
)

(define (square x) (* x x))

(define (pow b n)
  (if (= n 0)
  	1
  	(if (even? n)
  	(square (pow b (quotient n 2)))
  	(* b (pow b (- n 1)))))
)

(define (ordered? s)
  (if (null? s)
  	True
  	(if (null? (cdr s))
  		True
  		(and (or (<  (car s) (car (cdr s))) (=  (car s) (car (cdr s))))
  		     (ordered? (cdr s))))
))

(define (nodots s)
  (if (empty? s)
  	s
  	(if (number? (car s))
  		(if (number? (cdr s))
  			(cons (car s) (cons (cdr s) nil))
  			(cons (car s) (nodots (cdr s)))
  		)
  		(if (number? (cdr s))
  			(cons (nodots (car s)) (cons (cdr s) nil))
  			(cons (nodots (car s)) (nodots (cdr s)))
  		)
  	)
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) False)
          ((= (car s) v) True)
          ((< v (car s)) False)
          ((> v (car s)) (contains? (cdr s) v))
          (else nil)
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (if (empty? s) 
    	  (list v)
          (if (contains? s v)
          	s
          	(if (< v (car s))
          		(cons v s)
          		(cons (car s) (add (cdr s) v))))
          ))

(define (intersect s t)
    (if (or (empty? s) (empty? t)) 
    	   nil
          (if (= (car s) (car t))
          	(cons (car s) (intersect (cdr s) (cdr t)))
          	(if (< (car s) (car t))
          		(intersect (cdr s) t)
          		(intersect s (cdr t))
          ))))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (if (empty? s) 
    	   t
          (if (empty? t) 
          	s
          	(if (contains? t (car s))
          		(union (cdr s) t)
          		(union (cdr s) (add t (car s)))
          ; YOUR-CODE-HERE
          ))
          ))


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))

(define (in? t v)
    (if (empty? t) 
    	False
        (if (= (entry t) v)
        	True
        	(if (< v (entry t))
        		(in? (left t) v)
        		(in? (right t) v))
          
          ))
    )

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)
(define (leaf? t)
	(if (and (empty? (left t)) (empty? (right t)))
		True
		False))
(define (as-list t)
    (if (empty? t)
    	nil
    	(if (leaf? t)
    		(list (entry t))
    		(union (add (as-list (left t)) (entry t)) (as-list (right t))	
    	))
    )
)
