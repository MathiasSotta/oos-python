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

#exc1
def is_offered(courses, lecture_id, monthyear):
    q = courses[monthyear]

    if q:
        #print(q)
        for i in q:
            if i['lecture_id'] == lecture_id:
                return True

#exc2
def when_offered(courses, lecture_id):
    found = []
    for i in courses:
        q = courses[i]
        for j in q:
            if j['lecture_id'] == lecture_id:
                found.append(i)
    if found.__len__() > 0:
        return found
    else:
        return 'Course NOT in list'

def involved(courses, person):
    ls = []
    found = {}
    for i in courses:
        q = courses[i]
        for j in q:

            if j['teacher'] == person:
                    # cache course names found in current iteration
                    ls.append(j['lecture_id'])
                    # save courses of current iteration to dict
                    found[i] =  ls
        # reset list for next iteration
        ls = []

    if found.__len__() > 0:
        return found
    else:
        return 'Teacher NOT in list'

###########

# call exc1
print(is_offered(courses, 'NoSQL', 'mar2015'))
# call exc2
print(when_offered(courses, 'DB'))
# call exc3
print(involved(courses,'Preuss'))