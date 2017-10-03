courses = {
  'mar2014': (
            {
                   'lecture_id'	: 'P1',
                   'name'   : 'Programmierung I',
                   'author' : 'N.N.',
                   'teacher': 'Loose'
                   },
			{
                   'lecture_id'	: 'P2',
                   'name'   : 'Programmierung II',
                   'teacher': 'Loose',
                   'author' : 'N.N.',
                   'prereq' : 'P1'
                   },
			{
                   'lecture_id'	: 'DB',
                   'name'   : 'Datenbanken',
                   'teacher': 'Preuss',
                   'author' : 'Li'
                   }
           	),
  'sep2014': (
              {
                      'lecture_id'	: 'OOSL',
                      'name'   : 'OO Skriptsprachen',
                      'teacher': 'Preuss'
                      },
              {
	                  'lecture_id'	: 'DB',
                      'name'   : 'Datenbanken',
                      'teacher': 'Preuss',
                      'author':  'Li'
                      }
              ),
  'mar2015': (
              {       'lecture_id'	: 'NoSQL',
				      'name'   : 'NoSQL Datenbanken',
                      'teacher': 'Edlich'
                       },
              )
}

def is_offered(courses, lecture_id, monthyear):
    q = courses[monthyear]

    if q:
        #print(q)
        for i in q:
            if i['lecture_id'] == lecture_id:
                return True


print(is_offered(courses, 'NoSQL', 'mar2015'))
#print(is_offered(courses, 'NoSQL', 'sep2014'))
#print(is_offered(courses, 'P1', 'mar2015'))