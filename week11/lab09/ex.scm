(define (repeat k fn)
	(if (= k 1)
		(fn)
		(begin (fn) (repeat (- k 1) fn))))


(define (tri fn)
	(repeat 3 (lambda () (fn) (lt 120))))
(define (sier d k)
	(tri (lambda ()
		(if (= k 1)
			(fd d)
			(leg d k)))))

(define (leg d k)
	(sier (/ d 2) (- k 1))
	(penup)
	(fd d)
	(pendown))
(speed 0)
(sier 400 6)