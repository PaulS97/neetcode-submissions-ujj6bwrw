class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentLine = deque(students)
        matched = 1
        curr = 0

        while matched:
            matched = 0
            for i in range(len(studentLine)):
                print("students:", studentLine)
                print("sandwiches:", sandwiches)
                student = studentLine.popleft()
                sandwich = sandwiches[curr]
                if student == sandwich:
                    curr += 1
                    matched += 1
                else:
                    studentLine.append(student)

        return len(studentLine)




